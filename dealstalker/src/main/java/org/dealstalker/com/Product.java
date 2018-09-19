package org.dealstalker.com;

import java.sql.Date;
import java.util.List;
import java.util.Map;

public class Product {
	private Integer id;
	private String imageUrl;
	private String modelName;
	private String brandName;
	private String primaryCategory;
	private Float price;
	private Integer popularity;
	private String description;
	private String subCategory;
	private String priceCurrency;
	private String source;
	private String Resource;
	private int isDiscounted;
	private Gender gender;
	private String innerId;
	private String color;
	
	private List<Map<Date,Float>> stats;
	
	
	public enum Gender{
		Male,Female,Unisex
	}
	
	Product(){
		this.id = 0;
		this.imageUrl = "";
		this.modelName = "Cloth";
		this.brandName = "Unknown designer";
		this.price =  0.0F;
		this.primaryCategory = "";
		this.subCategory = "";
		this.gender = Gender.Unisex;
		this.isDiscounted = 0;
		this.priceCurrency = "USD";
	}
	
	public Integer getId() {
		return id;
	}
	public void setId(Integer id) {
		this.id = id;
	}
	public String getImageUrl() {
		return imageUrl;
	}
	public void setImageUrl(String imageUrl) {
		this.imageUrl = imageUrl;
	}
	public String getModelName() {
		return modelName;
	}
	public void setModelName(String modelName) {
		this.modelName = modelName;
	}
	public String getBrandName() {
		return brandName;
	}
	public void setBrandName(String brandName) {
		this.brandName = brandName;
	}
	public String getPrimaryCategory() {
		return primaryCategory;
	}
	public void setPrimaryCategory(String category) {
		this.primaryCategory = category;
	}
	public Float getPrice() {
		return price;
	}
	public void setPrice(Float price) {
		this.price = price;
	}
	public Integer getPopularity() {
		return popularity;
	}
	public void setPopularity(Integer popularity) {
		this.popularity = popularity;
	}
	public String getDescription() {
		return description;
	}
	public void setDescription(String description) {
		this.description = description;
	}
	public String getSubCategory() {
		return subCategory;
	}
	public void setSubCategory(String subCategory) {
		this.subCategory = subCategory;
	}
	public String getPriceCurrency() {
		return priceCurrency;
	}
	public void setPriceCurrency(String priceCurrency) {
		this.priceCurrency = priceCurrency;
	}
	public String getSource() {
		return source;
	}
	public void setSource(String source) {
		this.source = source;
	}
	public String getResource() {
		return Resource;
	}
	public void setResource(String resource) {
		Resource = resource;
	}
	public int getIsDiscounted() {
		return isDiscounted;
	}
	public void setIsDiscounted(int isDiscounted) {
		this.isDiscounted = isDiscounted;
	}
	public Gender getGender() {
		return gender;
	}
	public void setGender(Gender gender) {
		this.gender = gender;
	}	
	public void setGender(String gender) {
		switch(gender) {
			case "male" : this.gender = Gender.Male;
			case "female" : this.gender = Gender.Female;
			case "unisex" : this.gender = Gender.Unisex;	
		}
	}

	public String getInnerId() {
		return innerId;
	}

	public void setInnerId(String innerId) {
		this.innerId = innerId;
	}

	public String getColor() {
		return color;
	}

	public void setColor(String color) {
		this.color = color;
	}

	public List<Map<Date,Float>> getStats() {
		return stats;
	}

	public void setStats(List<Map<Date,Float>> stats) {
		this.stats = stats;
	}
}
