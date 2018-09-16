package org.dealstalker.com;

import java.util.List;

public class SearchEntry {
	private String searchQuery = "";
	private String gender = "";
	private String category = "";
	private String color = "";
	private String subCategory;
	private List<String> aSubCategory;  
	private List<String> bSubCategory;
	private List<String> cSubCategory;
	
	public String getSearchQuery() {
		return searchQuery;
	}
	public void setSearchQuery(String searchQuery) {
		this.searchQuery = searchQuery;
	}
	public String getGender() {
		return gender;
	}
	public void setGender(String gender) {
		this.gender = gender;
	}
	public String getCategory() {
		return category;
	}
	public void setCategory(String category) {
		this.category = category;
	}
	public String getColor() {
		return color;
	}
	public void setColor(String color) {
		this.color = color;
	}
	public String getSubCategory() {
		return subCategory;
	}
	public void setSubCategory(String subCategory) {
		this.subCategory = subCategory;
	}
	public List<String> getaSubCategory() {
		return aSubCategory;
	}
	public void setaSubCategory(List<String> aSubCategory) {
		this.aSubCategory = aSubCategory;
	}
	public List<String> getbSubCategory() {
		return bSubCategory;
	}
	public void setbSubCategory(List<String> bSubCategory) {
		this.bSubCategory = bSubCategory;
	}
	public List<String> getcSubCategory() {
		return cSubCategory;
	}
	public void setcSubCategory(List<String> cSubCategory) {
		this.cSubCategory = cSubCategory;
	}
}
