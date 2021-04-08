package de.grh_hamburg.eva.server.user.model;

import de.grh_hamburg.eva.server.dorm.model.Dormitory;
import de.grh_hamburg.eva.server.security.model.Role;
import de.grh_hamburg.eva.server.user.dto.UserDto;
import lombok.Data;
import lombok.NoArgsConstructor;

import javax.persistence.*;
import java.util.HashSet;
import java.util.Set;

@Data
@NoArgsConstructor
@Entity
@Table(name = "users")
public class User {
    @Id
    @Column(name = "user_id")
    @GeneratedValue(strategy = GenerationType.SEQUENCE)
    private Integer id;

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

    public User(UserDto dto, Dormitory dormitory) {
        this.userName = dto.getUserName();
        this.email = dto.getEmail();
        this.dormitory = dormitory;
        this.flat = dto.getFlat();
    }
}
