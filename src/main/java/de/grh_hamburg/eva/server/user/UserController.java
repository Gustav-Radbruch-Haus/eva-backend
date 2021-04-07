package de.grh_hamburg.eva.server.user;

import de.grh_hamburg.eva.server.user.model.User;
import de.grh_hamburg.eva.server.user.service.EvaUserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/")
public class UserController {
    @Autowired
    private EvaUserService userService;

    @GetMapping(value = "/users", produces = {"application/json"})
    public List<User> getAllUsers() {
        return userService.getAllUsers();
    }

    @GetMapping(value = "/users/{id}", produces = {"application/json"})
    public User getUserById(@PathVariable String id) {
        return userService.getUserById(id);
    }

    @PostMapping(value = "/users/createUser")
    public User createUser(@RequestBody String jsonUserObject) {
        // TODO ct, validate jsonUserObject and create new user
        return null;
    }
}
