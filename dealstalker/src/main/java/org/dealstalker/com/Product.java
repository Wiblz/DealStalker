package org.dealstalker.com;

public class Product {
	private Integer id;
	private String pathToImage;
	private String modelName;
	private String brandName;
	private String category;
	private Float lowerstPrice;
	private Float highestPrice;
	private Integer popularity;
	private String description;
	
	public Integer getId() {
		return id;
	}
	public void setId(Integer id) {
		this.id = id;
	}
	public String getPathToImage() {
		return pathToImage;
	}
	public void setPathToImage(String pathToImage) {
		this.pathToImage = pathToImage;
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
	public String getCategory() {
		return category;
	}
	public void setCategory(String category) {
		this.category = category;
	}
	public Float getLowerstPrice() {
		return lowerstPrice;
	}
	public void setLowerstPrice(Float lowerstPrice) {
		this.lowerstPrice = lowerstPrice;
	}
	public Float getHighestPrice() {
		return highestPrice;
	}
	public void setHighestPrice(Float highestPrice) {
		this.highestPrice = highestPrice;
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
}
