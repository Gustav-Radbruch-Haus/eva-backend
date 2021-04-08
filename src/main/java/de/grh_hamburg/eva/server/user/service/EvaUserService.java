package de.grh_hamburg.eva.server.user.service;

import com.fasterxml.jackson.core.JsonParseException;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import de.grh_hamburg.eva.server.dorm.model.Dormitory;
import de.grh_hamburg.eva.server.dorm.service.DormitoryService;
import de.grh_hamburg.eva.server.exception.BadRequestWhileCreateEntity;
import de.grh_hamburg.eva.server.exception.EntityNotFoundException;
import de.grh_hamburg.eva.server.exception.IdParseException;
import de.grh_hamburg.eva.server.user.dto.UserDto;
import de.grh_hamburg.eva.server.user.model.User;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Component;

import javax.persistence.EntityManager;
import javax.transaction.Transactional;
import java.util.List;

@Component
public class EvaUserService {
    private final Logger LOGGER = LoggerFactory.getLogger(EvaUserService.class);

    private final DormitoryService dormitoryService;
    private final UserRepository userRepository;
    private final PasswordEncoder passwordEncoder;
    private EntityManager entityManager = null;

    @Autowired
    public EvaUserService(DormitoryService dormitoryService, UserRepository userRepository,
                          PasswordEncoder passwordEncoder, EntityManager entityManager) {
        this.dormitoryService = dormitoryService;
        this.userRepository = userRepository;
        this.passwordEncoder = passwordEncoder;
        this.entityManager = entityManager;
    }

    public List<User> getAllUsers() {
        return userRepository.getAllUser();
    }

    public User getUserById(String id) {
        User user;

        try {
            user = userRepository.getUserById(Integer.parseInt(id));

            if (user == null) {
                LOGGER.error("Could not find user with ID : " + id);
                throw new EntityNotFoundException();
            }
        } catch (NumberFormatException e) {
            LOGGER.error("Could not parse id-string to integer : " + id);
            throw new IdParseException();
        }

        return user;
    }

    public User getUserByEMail(String email) {
        return userRepository.getUserByEMail(email);
    }

    @Transactional
    public User createUser(String jsonUserObject) {
        UserDto userDto;
        User user;

        try {
            userDto = new ObjectMapper().readValue(jsonUserObject, UserDto.class);
            user = new User(userDto);

            Dormitory dormitory = dormitoryService.getDormitoryById(userDto.getDormitoryId().toString());
            user.setDormitory(dormitory);
            user.setPassHash(this.passwordEncoder.encode(userDto.getPassword()));

        } catch (JsonParseException jpe) {
            LOGGER.error("Could not deserialize input-json, for unknown reason" + jpe.getMessage());
            throw new BadRequestWhileCreateEntity();
        } catch (JsonProcessingException jpe) {
            LOGGER.error("Could not process json. " + jpe.getMessage());
            throw new BadRequestWhileCreateEntity();
        }

        entityManager.persist(user);
        entityManager.flush();

        return user;
    }
}
