package de.grh_hamburg.eva.server.user.model;

import de.grh_hamburg.eva.server.dorm.model.Dormitory;
import de.grh_hamburg.eva.server.security.model.Role;
import lombok.Data;

import javax.persistence.*;
import java.util.HashSet;
import java.util.Set;

@Data
@Entity
@Table(name = "users")
public class User {
    @Id
    @Column(name = "user_id")
    @GeneratedValue(strategy = GenerationType.SEQUENCE)
    private Long id;

    @Column(name = "email")
    private String email;

    @Column(name = "full_name")
    private String userName;

    @OneToOne
    @JoinColumn(name = "dormitory_id")
    private Dormitory dormitory;

    @Column(name = "flat")
    private String flat;

    @Column(name = "password_hash")
    private String passHash;

    @Column(name = "salt")
    private String salt;

    @Column(name = "enabled")
    private Boolean enabled;

    @Column(name = "comment")
    private String comment;

    @ManyToMany(cascade = CascadeType.ALL, fetch = FetchType.EAGER)
    @JoinTable(
            name = "users_roles",
            joinColumns = @JoinColumn(name = "user_id"),
            inverseJoinColumns = @JoinColumn(name = "role_id")
    )
    private Set<Role> roles = new HashSet<>();

    public User() {
    }
}
