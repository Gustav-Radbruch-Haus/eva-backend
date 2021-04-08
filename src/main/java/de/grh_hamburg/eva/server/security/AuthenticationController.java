package de.grh_hamburg.eva.server.security;

import de.grh_hamburg.eva.server.security.service.AuthenticationService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/authentication/")
public class AuthenticationController {

    @Autowired
    private AuthenticationService authenticationService;


    @PostMapping(value = "/login")
    public void loginUser(@RequestBody String credentialUserJson) {
        authenticationService.authenticateUser(credentialUserJson);
    }
}
