package de.grh_hamburg.eva.server.user.dto;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class UserDto {
    private String email;
    private String userName;
    private Integer dormitoryId;
    private String flat;
    private String password;
}
