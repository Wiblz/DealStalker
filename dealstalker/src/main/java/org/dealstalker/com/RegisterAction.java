package org.dealstalker.com;

import com.opensymphony.xwork2.ActionSupport;

public class RegisterAction extends ActionSupport {
    
    private static final long serialVersionUID = 1L;
    
    private Customer customerBean;


    public String execute() throws Exception {
    	int i = RegisterDAO.save(this);  
        if (i > 0) {  
        	return "success";  
        }  
        return "error"; 
    }
    
    public Customer getCustomerBean() {
        return customerBean;
    }
    
    public void setCustomerBean(Customer customer) {
    	customerBean = customer;
    }
}
