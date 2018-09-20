package org.dealstalker.com;

import java.sql.SQLException;
import java.util.Map;

import javax.servlet.http.HttpServletRequest;

import org.apache.struts2.ServletActionContext;
import org.apache.struts2.interceptor.RequestAware;
import org.apache.struts2.interceptor.ServletRequestAware;

import com.opensymphony.xwork2.ActionSupport;

public class ItemInfo extends ActionSupport {
	
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	public int id = -1; 
	Product currentProduct;
	public String execute() {
		id = Integer.parseInt(ServletActionContext.getRequest().getParameter("id"));
		try {
			 currentProduct = SearchEngine.getProductItem(id);
		} catch (SQLException e) {
			e.printStackTrace();
			System.out.println("Error during aquiring product item from db");
		}
		
		currentProduct.setStats(SearchEngine.getStats(currentProduct.getInnerId(), currentProduct.getColor()));	
		return SUCCESS;
	}
	
	public void setid(int id) {
		this.id = id;
	}
	
	public int getId() {
		return this.id;
	}	
	
	public void setCurrentProduct(Product p) {
		this.currentProduct = p;
	}
	
	public Product getCurrentProduct() {
		return this.currentProduct;
	}
}
