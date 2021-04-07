package de.grh_hamburg.eva.server.security;

import de.grh_hamburg.eva.server.security.service.EvaUserDetailsService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/authentication")
public class AuthenticationController {

    @Autowired
    private EvaUserDetailsService userDetailsService;
}
