/*
 * Copyright 2006 The Apache Software Foundation.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package org.dealstalker.com;


import com.opensymphony.xwork2.ActionSupport;


import java.util.ArrayList;
import java.util.Arrays;
import java.util.Date;
import java.util.List;
import java.util.Map;

import javax.servlet.http.HttpSession;

import org.apache.struts2.ServletActionContext;
import org.apache.struts2.interceptor.SessionAware;

import com.opensymphony.xwork2.conversion.annotations.Conversion;
import com.opensymphony.xwork2.conversion.annotations.TypeConversion;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;


/**
 * 
 */
@Conversion()
public class IndexAction extends ActionSupport implements SessionAware{
	
	
	
	private ArrayList<Product> productList; 
	public Integer currentPage = 0;
	public Integer productPerPage = 50;
	
	private Map<String, Object> userSession;
	
	public SearchEntry entry;
	public List<String> categories =  Arrays.asList("Clothing","Shoes","Accessories");
	public List<String> genders = Arrays.asList("Male","Female","Doesn`t matter!");
	
	public List<String> cCat = Arrays.asList();
	public List<String> bCat = Arrays.asList();	
	public List<String> aCat = Arrays.asList();
	
	public List<String> subCategories = new ArrayList<String>();
	
	
    public String execute() throws Exception {  
    	userSession.put("page", currentPage);
        return SUCCESS;
    }
    
    public String search() throws Exception {      
        Connection cnx = DriverLoader.getMySqlConnection();
        Statement stmt = null;
        String query = "Select * from Products LIMIT 10000;";
        
        
        SearchEntry entr = (SearchEntry) userSession.get("entry");
        productList = SearchEngine.Search((SearchEntry) userSession.get("entry"));
        
        userSession.put("list", productList);
        setCategories(entry);

        
        return SUCCESS;
    }
    
    public String nextPage() throws Exception {  
    	productList = ((ArrayList<Product>) userSession.get("list"));
    	if(productList.size() != 0) {
    		currentPage = (int)userSession.get("page");
            if((currentPage+1)*50 >= productList.size())
            	return SUCCESS;	
            currentPage++;
    		userSession.put("page", currentPage);
    	}
    	
    	System.out.println(currentPage);
    	return SUCCESS;
    }
    
    public String prevPage() throws Exception {
    	productList = (ArrayList<Product>) userSession.get("list");
    	currentPage = (int)userSession.get("page");
    	if(currentPage == 0)
    		return SUCCESS;
    	currentPage--;
    	userSession.put("page", currentPage);
        return SUCCESS;
    }
    
    
    public void setEntry(SearchEntry s) {
    	this.entry = s;
    	if(entry.getGender().equals("w"))
    		appendToWomenCat();
    	userSession.put("entry", entry);
    }
    
    public SearchEntry getEntry() {
    	return this.entry;
    }
    
    public List<Product> getProductList() {
    	if(productList.size() == 0)
    		return productList; 	
    	return  
    		 productList.subList(currentPage * 50, 
			 ((currentPage + 1) * 50 < productList.size()) ? 
					(currentPage+1) * 50 : productList.size() - 1);
    }
    
    public void setProductList(ArrayList<Product> productList) {
    	this.productList = productList;
    }

	@Override
	public void setSession(Map<String, Object> session) {
		userSession = session;
	}
	
	public void setCategories(SearchEntry entry) {
		if(entry.getGender().equals("Female")) {
			cCat = Arrays.asList( "Activewear" ,
					"Jackets & Coats" ,"Hoodies & Sweatshirts" ,"Jeans & Trousers" ,
					"Shirts" ,"T-shirts" ,"Shorts" ,"Loungewear","Swimming stuff","Lingerie & Nightwear & Kimonos",
					"Loungewear","Skirts","Tops","Swimming wear");
			
			 bCat = Arrays.asList("Boots", "Shoes","Sanadals, Sliders & Flip Flpos" ,"Sneakers & Trainers");
			
			 aCat = Arrays.asList("Wallets & Purses","Socks & Tights" ,"Bags" ,
						"Belts & Braces" ,"Hats & Caps" ,"Ties" ,"Glasses"  ,
						"Gloves and Scarfs","Underwear" ,"Not really useful stuff", "Bra","Hair accessories");
		}
		else {
			cCat = Arrays.asList( "Activewear" ,
					"Jackets & Coats" ,"Hoodies & Sweatshirts" ,"Jeans & Trousers" ,
					"Shirts" ,"T-shirts" ,"Shorts" ,"Loungewear","Swimming stuff");
			
			 bCat = Arrays.asList("Boots", "Shoes","Sanadals, Sliders & Flip Flpos" ,"Sneakers & Trainers");
			
			 aCat = Arrays.asList("Wallets & Purses","Socks" ,"Bags" ,
						"Belts & Braces" ,"Hats & Caps" ,"Ties" ,"Glasses"  ,
						"Gloves and Scarfs","Underwear" ,"Not really useful stuff");
		}
	}
    
	
	public void appendToWomenCat() {
		for(String s: entry.getaSubCategory()) {
			StringBuilder b = new StringBuilder(s);
			s = b.append(" [W]").toString();
		}
		for(String s: entry.getbSubCategory()) {
			StringBuilder b = new StringBuilder(s);
			s = b.append(" [W]").toString();
		}
		for(String s: entry.getcSubCategory()) {
			StringBuilder b = new StringBuilder(s);
			s = b.append(" [W]").toString();
		}
	}
}
