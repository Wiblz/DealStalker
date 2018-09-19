package org.dealstalker.com;

import com.opensymphony.xwork2.ActionSupport;

public class RegisterAction extends ActionSupport {
    
    private static final long serialVersionUID = 1L;
    
    private Customer customerBean;

    public String execute() throws Exception {
    	int i = RegisterDAO.save(this);  
        if (i > 0) {  
        	return "success";  
        } else if (i == RegisterDAO.LOGIN_IS_TAKEN) {
        	return "taken";
        }
        return "error";
    }
    
    public void validate() {
	    if (customerBean.getLogin().length() < 4 || customerBean.getLogin().length() > 32) {
	        addFieldError("personBean.Login", "Login length should be between 4 and 32 characters.");
	        System.out.println(customerBean.getLogin());
	    }
	
	    if (customerBean.getEmail().length() == 0) {
	        addFieldError("personBean.email", "Email is required.");
	        System.out.println(customerBean.getEmail());
	    }
	    
	    if (!customerBean.getPassword().equals(customerBean.getRepeatedPassword())) {
	        addFieldError("personBean.repeatedPassword", "Password should be identical");
	        System.out.println(customerBean.getPassword() + "\n" + customerBean.getRepeatedPassword());
	    }
    }
    
    public Customer getCustomerBean() {
        return customerBean;
    }
    
    public void setCustomerBean(Customer customer) {
    	customerBean = customer;
    }
}
