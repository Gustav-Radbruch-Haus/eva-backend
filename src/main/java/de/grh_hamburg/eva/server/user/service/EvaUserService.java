package de.grh_hamburg.eva.server.user.service;

import de.grh_hamburg.eva.server.user.model.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.util.List;

@Component
public class EvaUserService {
    @Autowired
    private UserRepository userRepository;

    public List<User> getAllUsers() {
        return userRepository.getAllUser();
    }

    public User getUserById(String id) {
        int intId;

        try {
            intId = Integer.parseInt(id);
        } catch (NumberFormatException e) {
            return null;
        }

        return userRepository.getUserById(intId);
    }

    public User getUserByEMail(String email) {
        return userRepository.getUserByEMail(email);
    }
}
