package de.grh_hamburg.eva.server.user.service;

import de.grh_hamburg.eva.server.user.model.User;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import java.util.List;

public interface UserRepository extends JpaRepository<User, Integer> {

    @Query("SELECT u FROM User u WHERE u.userName = :username")
    User getUserByUsername(@Param("username") String username);

    @Query("SELECT u FROM User u WHERE u.id = :id")
    User getUserById(@Param("id") Integer id);

    @Query("SELECT u FROM User u WHERE u.email = :email")
    User getUserByEMail(@Param("email") String email);

    @Query("SELECT u FROM User u")
    List<User> getAllUser();
}
