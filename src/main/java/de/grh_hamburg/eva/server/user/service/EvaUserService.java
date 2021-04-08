package de.grh_hamburg.eva.server.user.service;

import de.grh_hamburg.eva.server.exception.EntityNotFoundException;
import de.grh_hamburg.eva.server.exception.IdParseException;
import de.grh_hamburg.eva.server.user.model.User;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.util.List;

@Component
public class EvaUserService {
    private final Logger LOGGER = LoggerFactory.getLogger(EvaUserService.class);

    @Autowired
    private UserRepository userRepository;

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
}
