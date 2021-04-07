package de.grh_hamburg.eva.server.user.service;

import de.grh_hamburg.eva.server.user.model.User;
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<User, Integer> {
}
