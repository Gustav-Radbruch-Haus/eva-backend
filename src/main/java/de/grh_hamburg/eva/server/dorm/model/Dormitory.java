package de.grh_hamburg.eva.server.dorm.model;

import lombok.Data;

import javax.persistence.*;

@Data
@Entity
@Table(name = "dormitories")
public class Dormitory {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long id;

    @Column(name = "name")
    private String dormName;

    @OneToOne
    @JoinColumn(name = "address_id")
    private Address address;

    public Dormitory() {
    }

    @Override
    public String toString() {
        return "Dormitory{" +
                "id=" + id +
                ", dormName='" + dormName + '\'' +
                ", address=" + address +
                '}';
    }
}
