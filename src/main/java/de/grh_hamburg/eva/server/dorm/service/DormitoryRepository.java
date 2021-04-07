package de.grh_hamburg.eva.server.dorm.service;

import de.grh_hamburg.eva.server.dorm.model.Dormitory;
import org.springframework.data.jpa.repository.JpaRepository;

public interface DormitoryRepository extends JpaRepository<Dormitory, Integer> {
}
