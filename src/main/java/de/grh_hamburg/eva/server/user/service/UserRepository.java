package de.grh_hamburg.eva.server.user.service;

import de.grh_hamburg.eva.server.user.model.User;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

public interface UserRepository extends JpaRepository<User, Integer> {

    @Query("SELECT u FROM User u WHERE u.userName = :username")
    User getUserByUsername(@Param("username") String username);
}
