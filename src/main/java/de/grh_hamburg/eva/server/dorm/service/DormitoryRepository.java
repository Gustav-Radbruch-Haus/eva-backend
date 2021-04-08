package de.grh_hamburg.eva.server.dorm.service;

import de.grh_hamburg.eva.server.dorm.model.Dormitory;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import java.util.List;

public interface DormitoryRepository extends JpaRepository<Dormitory, Integer> {

    @Query("SELECT d FROM Dormitory d WHERE d.dormName = :dormName")
    Dormitory getDormitoryByName(@Param("dormName") String dormName);

    @Query("SELECT d FROM Dormitory d WHERE d.id = :dormId")
    Dormitory getDormitoryById(@Param("dormId") Integer dormId);

    @Query("SELECT d FROM Dormitory d")
    List<Dormitory> getAllDormitories();
}
