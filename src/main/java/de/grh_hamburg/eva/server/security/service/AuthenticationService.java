package de.grh_hamburg.eva.server.security.service;

import com.fasterxml.jackson.core.JsonParseException;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import de.grh_hamburg.eva.server.exception.AccessForbiddenException;
import de.grh_hamburg.eva.server.exception.BadRequestWhileCreateEntity;
import de.grh_hamburg.eva.server.exception.EntityNotFoundException;
import de.grh_hamburg.eva.server.user.dto.UserDto;
import de.grh_hamburg.eva.server.user.model.User;
import de.grh_hamburg.eva.server.user.service.EvaUserService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Component;

@Component
public class AuthenticationService {
    private final Logger LOGGER = LoggerFactory.getLogger(AuthenticationService.class);

    private final EvaUserService evaUserService;
    private final PasswordEncoder passwordEncoder;

    @Autowired
    public AuthenticationService(EvaUserService evaUserService, PasswordEncoder passwordEncoder) {
        this.evaUserService = evaUserService;
        this.passwordEncoder = passwordEncoder;
    }


    public void authenticateUser(String credentialUserJson) {
        UserDto userDto;
        User user;

        try {
            userDto = new ObjectMapper().readValue(credentialUserJson, UserDto.class);
            user = evaUserService.getUserByEMail(userDto.getEmail());

            if (user == null) {
                throw new EntityNotFoundException();
            }

            if (!passwordEncoder.matches(passwordEncoder.encode(userDto.getPassword()), user.getPassHash())) {
                throw new AccessForbiddenException();
            }
        } catch (JsonParseException jpe) {
            LOGGER.error("Could not deserialize input-json, for unknown reason" + jpe.getMessage());
            throw new BadRequestWhileCreateEntity();
        } catch (JsonProcessingException jpe) {
            LOGGER.error("Could not process json. " + jpe.getMessage());
            throw new BadRequestWhileCreateEntity();
        }

        // TODO ct, 08.04.2021 - return what? bearer token? .. need to read stuff
    }
}
