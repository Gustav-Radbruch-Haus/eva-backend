package de.grh_hamburg.eva.server.dorm.service;

import de.grh_hamburg.eva.server.dorm.model.Dormitory;
import de.grh_hamburg.eva.server.exception.EntityNotFoundException;
import de.grh_hamburg.eva.server.exception.IdParseException;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.util.List;

@Component
public class DormitoryService {
    private final Logger LOGGER = LoggerFactory.getLogger(DormitoryService.class);

    @Autowired
    private DormitoryRepository dormitoryRepository;

    public List<Dormitory> getAllDormitories() {
        return dormitoryRepository.getAllDormitories();
    }

    public Dormitory getDormitoryById(String id) {
        int intId;
        Dormitory dormitory;

        try {
            intId = Integer.parseInt(id);
            dormitory = dormitoryRepository.getDormitoryById(intId);

            if (dormitory == null) {
                LOGGER.error("Could not find dormitory with ID : " + id);
                throw new EntityNotFoundException();
            }
        } catch (NumberFormatException e) {
            LOGGER.error("Could not parse id-string to integer : " + id);
            throw new IdParseException();
        }

        return dormitory;
    }

    public Dormitory getDormitoryByName(String name) {
        Dormitory dormitory = dormitoryRepository.getDormitoryByName(name);

        if (dormitory == null) {
            LOGGER.error("Could not find dormitory with name : " + name);
            throw new EntityNotFoundException();
        }

        return dormitory;
    }
}
