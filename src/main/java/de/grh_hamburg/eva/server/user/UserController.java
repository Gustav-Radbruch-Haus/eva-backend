package de.grh_hamburg.eva.server.user;

import de.grh_hamburg.eva.server.user.service.EvaUserDetailsService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class UserController {

    @Autowired
    private EvaUserDetailsService userDetailsService;

    @GetMapping("/test")
    public String test() {
        UserDetails userDetails = userDetailsService.loadUserByUsername("Chris Thiele");
        return "Test";
    }
}
