package de.grh_hamburg.eva.server.security.model;

import lombok.Data;

import javax.persistence.*;

@Data
@Entity
@Table(name = "roles")
public class Role {
    @Id
    @Column(name = "role_id")
    @GeneratedValue(strategy = GenerationType.SEQUENCE)
    private int roleId;

    @Column(name = "name")
    private String roleName;

    public Role() {
    }
}
