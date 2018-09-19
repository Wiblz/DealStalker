package org.dealstalker.com;

public class Customer {
    private String login = "";
    private String email = "";
    private String password = "";
    private String repeatedPassword = "";

    public String getLogin() {
        return login;
    }

    public void setLogin(String login) {
        this.login = login;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        	this.email = email;
    }
	
    public String getRepeatedPassword() {
        return repeatedPassword;
    }

    public void setRepeatedPassword(String repeatedPassword) {
        this.repeatedPassword = repeatedPassword;
    }
    
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public String toString() {
        return "First Name: " + getLogin() + "\n"  +
        " Email:      " + getEmail();
    }

}


