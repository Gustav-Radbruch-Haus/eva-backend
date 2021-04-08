package de.grh_hamburg.eva.server.user;

import de.grh_hamburg.eva.server.user.model.User;
import de.grh_hamburg.eva.server.user.service.EvaUserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/")
public class UserController {
    //FIXME ct, 08.04.2021 - (all) controller should return dto objects not db models.

    @Autowired
    private EvaUserService userService;

    @GetMapping(value = "/users", produces = {"application/json"})
    public List<User> getAllUsers() {
        return userService.getAllUsers();
    }

    @PostMapping(value = "/users", consumes = {"application/json"}, produces = {"application/json"})
    public User createUser(@RequestBody String jsonUserObject) {
        System.out.println(jsonUserObject);
        return userService.createUser(jsonUserObject);
    }

    @GetMapping(value = "/users/{id}", produces = {"application/json"})
    public User getUserById(@PathVariable String id) {
        return userService.getUserById(id);
    }
}
