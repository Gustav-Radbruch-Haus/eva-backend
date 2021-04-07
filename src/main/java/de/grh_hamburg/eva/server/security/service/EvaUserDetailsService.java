package de.grh_hamburg.eva.server.security.service;

import de.grh_hamburg.eva.server.user.model.EvaUserDetails;
import de.grh_hamburg.eva.server.user.model.User;
import de.grh_hamburg.eva.server.user.service.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Component;

@Component
public class EvaUserDetailsService implements UserDetailsService {

    @Autowired
    private UserRepository userRepository;

    public EvaUserDetailsService() {
    }

    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        User user = userRepository.getUserByUsername(username);

        if (user == null) {
            throw new UsernameNotFoundException("Could not find User!");
        }

        return new EvaUserDetails(user);
    }
}
