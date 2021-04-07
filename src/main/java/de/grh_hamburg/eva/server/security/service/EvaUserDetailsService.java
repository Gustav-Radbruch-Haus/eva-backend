package de.grh_hamburg.eva.server.security.service;

import de.grh_hamburg.eva.server.user.model.User;
import org.springframework.security.core.userdetails.User.UserBuilder;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;

public class EvaUserDetailsService implements UserDetailsService {


    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        User user = getUserByUserName(username);
        UserBuilder userBuilder = null;

        if (user != null) {

        }

        return null;
    }

    // TODO ct, 28.03.2021 need to be replaced with db query, dummy method just for testing
    private User getUserByUserName(String userName) {
        if (userName.equals("admin")) {
            return new User();
        }

        return null;
    }
}
