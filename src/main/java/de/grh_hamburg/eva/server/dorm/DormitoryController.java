package de.grh_hamburg.eva.server.dorm;

import de.grh_hamburg.eva.server.dorm.model.Dormitory;
import de.grh_hamburg.eva.server.dorm.service.DormitoryService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping(value = "/api/")
public class DormitoryController {
    @Autowired
    private DormitoryService dormitoryService;

    @GetMapping(value = "/dormitories", produces = {"application/json"})
    public List<Dormitory> getAllDormitories() {
        return dormitoryService.getAllDormitories();
    }

    @GetMapping(value = "/dormitories/{id}", produces = {"application/json"})
    public Dormitory getDormitoryById(@PathVariable String id) {
        return dormitoryService.getDormitoryById(id);
    }
}
