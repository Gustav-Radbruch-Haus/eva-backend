package de.grh_hamburg.eva.server.security.filter;

import de.grh_hamburg.eva.server.security.service.EvaUserDetailsService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.security.web.authentication.UsernamePasswordAuthenticationFilter;

public class AuthTokenFilter extends UsernamePasswordAuthenticationFilter {
    private final Logger LOGGER = LoggerFactory.getLogger(AuthTokenFilter.class);

    private EvaUserDetailsService userDetailsService;
    

}
