package de.grh_hamburg.eva.server.dorm.model;

import lombok.Data;

import javax.persistence.*;

@Data
@Entity
@Table(name = "addresses")
public class Address {
    @Id
    @Column(name = "address_id")
    @GeneratedValue(strategy = GenerationType.SEQUENCE)
    private Integer addressId;

    @Column(name = "street")
    private String street;

    @Column(name = "street_number")
    private Integer streetNumber;

    @Column(name = "city")
    private String city;

    @Column(name = "postal_code")
    private String postalCode;

    @Column(name = "country_iso")
    private String countryIso; // ISO 3166-1 alpha-2

    @Column(name = "comment")
    private String comment;

    public Address() {
    }
}
