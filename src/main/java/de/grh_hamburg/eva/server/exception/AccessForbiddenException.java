package de.grh_hamburg.eva.server.exception;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ResponseStatus;

@ResponseStatus(code = HttpStatus.FORBIDDEN, reason = "Something went wrong, wrong credentials?")
public class AccessForbiddenException extends RuntimeException {
}
