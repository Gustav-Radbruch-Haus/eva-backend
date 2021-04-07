package de.grh_hamburg.eva.server.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.core.userdetails.UserDetailsService;

@Configuration
@EnableWebSecurity
public class WebSecurityConfig extends WebSecurityConfigurerAdapter {

    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http.authorizeRequests()
                .antMatchers("/", "/hello-world").permitAll()
                .anyRequest().authenticated().and()
                .formLogin().loginPage("/login").permitAll().and()
                .logout().permitAll();
    }

    @Bean
    @Override
    protected UserDetailsService userDetailsService() {
        // TODO ct 21.11.2020 ; implement custom UserDetailsServices
        return super.userDetailsService();
    }
}
