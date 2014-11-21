########Ruby Syntax
########Controller Methods
class PagesController < ApplicationController
 def home
 end
 def erb_demo
 end
 def render_demo
  render :home
 end
  def redirect_demo
 redirect_to(:action => 'home')
 end
end

########Routes

Rails.application.routes.draw do
  get '/' => 'pages#home'

  resources :categories
  get 'categories/:id/delete' => 'categories#delete', :as => :categories_delete
end



######## Views
<%= render 'shared/topnav' %>

<div class="jumbotron">
  <div class="container">
    <div class="row">
      <div class="col-md-6">
        <h1>Shop directly from people around the world.</h1>
      </div>
    </div>
  </div>
</div>

<div class="trending">
  <div class="container">
    <h2>Recent Favorites</h2>
    <p>Discover finds from around the marketplace.</p>
    <div class="row trending-listing">
      <div class="col-md-4">
        <div class="thumbnail">
          <img src="https://img1.etsystatic.com/034/0/6705395/il_340x270.542888787_ggy4.jpg">
          <div class="caption">
            <span class="listing-title">Large gold leather bag</span>
            <span class="listing-price">$100.00</span>
          </div>
        </div>
      </div>
      <div class="col-md-4">
        <div class="thumbnail">
          <img src="https://img1.etsystatic.com/010/0/6957353/il_340x270.427320275_pxiv.jpg">
          <div class="caption">
            <span class="listing-title">Large gold leather bag</span>
            <span class="listing-price">$15.00</span>
          </div>
        </div>
      </div>
      <div class="col-md-4">
        <div class="thumbnail">
          <img src="https://img1.etsystatic.com/038/0/6566540/il_340x270.566511947_1r1t.jpg">
          <div class="caption">
            <span class="listing-title">Large gold leather bag</span>
            <span class="listing-price">$160.00</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<%= render 'shared/footer' %>




########ERB

class PagesController < ApplicationController
 def home
 end
 def erb_demo
 end
 def render_demo
  render :home
 end
  def redirect_demo
 redirect_to(:action => 'home')
 end
end


########Rendering

class PagesController < ApplicationController
 def home
 end
 def erb_demo
 end
 def render_demo
  render :home
 end
  def redirect_demo
 redirect_to(:action => 'home')
 end
end


########Redirecting

class PagesController < ApplicationController
 def home
 end
 def erb_demo
 end
 def render_demo
  render :home
 end
  def redirect_demo
 redirect_to(:action => 'home')
 end
end

########Congratulations

class PagesController < ApplicationController
 def home
 end
 def erb_demo
 end
 def render_demo
  render :home
 end
  def redirect_demo
 redirect_to(:action => 'home')
 end
end


########Migrating your Database

class CreateCategories < ActiveRecord::Migration
  def change
    create_table :categories do |t|
			t.string :name
			t.string :thumburl
      t.timestamps
    end
  end
end


########Seeding the Database

# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rake db:seed (or created alongside the db with db:setup).
#
# Examples:
#
#   cities = City.create([{ name: 'Chicago' }, { name: 'Copenhagen' }])
#   Mayor.create(name: 'Emanuel', city: cities.first)

	art = Category.create(name: 'Art', thumburl: 'http://upload.wikimedia.org/wikipedia/commons/e/eb/144-la_fuente_de_Monforte_V.jpg')
	home_and_living = Category.create(name: 'Home & Living', thumburl: 'http://ihomedecorsideas.com/wp-content/uploads/2014/04/diy_network_homemade_coat_rack_.jpg')
	jewelry = Category.create(name: 'Jewelry', thumburl: 'http://upload.wikimedia.org/wikipedia/commons/f/ff/Midyat_Silver_Jewelry_1310103_Nevit.jpg')
	women = Category.create(name: 'Women', thumburl: 'https://c1.staticflickr.com/9/8255/8660920433_57a184d9d1_z.jpg')
	men = Category.create(name: 'Men', thumburl: 'http://upload.wikimedia.org/wikipedia/commons/d/d5/Fullbrogue_(Grenson).jpg')
	kids = Category.create(name: 'Kids', thumburl: 'http://upload.wikimedia.org/wikipedia/commons/e/e0/Artist%27s_Paint_Brushes_Adapted_With_Photoshop._Surrey_UK.jpg')
	vintage = Category.create(name: 'Vintage', thumburl: 'https://c2.staticflickr.com/8/7402/9426557291_139134efaa_z.jpg')
	weddings = Category.create(name: 'Weddings', thumburl: 'http://hostingessence.com/wp-content/uploads/2012/04/green-wedding.jpg')
 craft_supplies = Category.create(name: 'Craft Supplies', thumburl:'http://bit.ly/1w1uPow')  # Add your category here


########Strong Params
class CategoriesController < ApplicationController
  def index
   @categories = Category.all
  end

  def show
   @category = Category.find(params[:id])
  end

  def new
  @category = Category.new
  end
  def create 
  @category = Category.new(category_params)
  if @category.save
   redirect_to(:action => 'index')
   else
   render('new')
   end
  end

  def edit
  @category = Category.find(params[:id])
  end
	def update
	@category = Category.find(params[:id])
  if @category.update_attributes(category_params)
    redirect_to(:action => 'show', :id => @category.id)
  else
    render('index')
  end	
	end
	def destroy
	Category.find(params[:id]).destroy
  redirect_to(:action => 'index')
	end
  def delete
  @category = Category.find(params[:id])
  end
  private
  def category_params
   params.require(:category).permit(:name, :thumburl)
   end
end



########Index
class CategoriesController < ApplicationController
  def index
   @categories = Category.all
  end

  def show
   @category = Category.find(params[:id])
  end

  def new
  @category = Category.new
  end
  def create 
  @category = Category.new(category_params)
  if @category.save
   redirect_to(:action => 'index')
   else
   render('new')
   end
  end

  def edit
  @category = Category.find(params[:id])
  end
	def update
	@category = Category.find(params[:id])
  if @category.update_attributes(category_params)
    redirect_to(:action => 'show', :id => @category.id)
  else
    render('index')
  end	
	end
	def destroy
	Category.find(params[:id]).destroy
  redirect_to(:action => 'index')
	end
  def delete
  @category = Category.find(params[:id])
  end
  private
  def category_params
   params.require(:category).permit(:name, :thumburl)
   end
end


########Index Route
Rails.application.routes.draw do
  get '/' => 'pages#home'

  resources :categories
  get 'categories/:id/delete' => 'categories#delete', :as => :categories_delete
end


########Index View
<%= render 'shared/topnav' %>

<div class="categories">
      <div class="container">
        <div class="row">
          <div class="col-md-2">
            <h2>Categories</h2>
            <p>Explore our latest categories from around the world.</p>
          </div>
          <div class="col-md-8">
            <% @categories.in_groups_of(3).each do |categories| %>
              <% categories.select! {|x| !x.nil?} %>
              <div class='row'>
                <% categories.each do |category| %>
                  <div class='col-md-4'>
                    <div class="thumbnail">
                        <img src= <%= category.thumburl %> >
                        <div class="caption">
                          <span class="listing-title"><%= category.name %></span>
                          <span><%= link_to "Edit", edit_category_path(category.id) %></span>
                          <span><%= link_to 'Show', category %></span>
                          <td><%= link_to 'Delete', categories_delete_path(:id => category.id) %></td>
                        </div>
                      </div>
                    </div>
                <% end %>
              </div>
            <% end %>

          </div>
        </div>

      </div>
    </div>

<table>
  <thead>
    <tr>
      <th>Category name</th>
      <th colspan="3"></th>
    </tr>
  </thead>

  <tbody>
    <% @categories.each do |category| %>
      <tr>
        <td><%= category.name %></td>
        <div class="thumbnail">
           <img src= <%=category.thumburl %> >
        <div>
        <td><%= link_to 'Show', category %></td>
        <td><%= link_to 'Edit', edit_category_path(category) %></td>
        <td><%= link_to 'Delete', categories_delete_path(:id => category.id) %></td>
      </tr>
    <% end %>
  </tbody>
</table>
<br>

<%= link_to 'New Category', new_category_path %>

<%= render 'shared/footer' %>

########Show Categories
class CategoriesController < ApplicationController
  def index
   @categories = Category.all
  end

  def show
   @category = Category.find(params[:id])
  end

  def new
  @category = Category.new
  end
  def create 
  @category = Category.new(category_params)
  if @category.save
   redirect_to(:action => 'index')
   else
   render('new')
   end
  end

  def edit
  @category = Category.find(params[:id])
  end
	def update
	@category = Category.find(params[:id])
  if @category.update_attributes(category_params)
    redirect_to(:action => 'show', :id => @category.id)
  else
    render('index')
  end	
	end
	def destroy
	Category.find(params[:id]).destroy
  redirect_to(:action => 'index')
	end
  def delete
  @category = Category.find(params[:id])
  end
  private
  def category_params
   params.require(:category).permit(:name, :thumburl)
   end
end

########Show Route
Rails.application.routes.draw do
  get '/' => 'pages#home'

  resources :categories
  get 'categories/:id/delete' => 'categories#delete', :as => :categories_delete
end

########Show View
<%= render 'shared/topnav' %>
<p>
  <strong>Name:</strong>
  <%= @category.name %>
</p>

<p>
  <strong>Thumburl:</strong>
  <%= image_tag @category.thumburl %>
</p>

<%= link_to 'Edit', edit_category_path(@category) %> |
<%= link_to 'Back', categories_path %>

<%= render 'shared/footer' %>

########Forms
<%= form_for(@category) do |f| %>

  <div class="name">
  <%= f.label :name %><br>
  <%= f.text_field :name %>
  </div>
  <div class="thumburl">
  <%= f.label :thumburl %><br>
  <%= f.text_field :thumburl %>
  </div>
  <div class="actions">
	<%= f.submit %>
  </div>
<% end %>

########New and Create Methods
class CategoriesController < ApplicationController
  def index
   @categories = Category.all
  end

  def show
   @category = Category.find(params[:id])
  end

  def new
  @category = Category.new
  end
  def create 
  @category = Category.new(category_params)
  if @category.save
   redirect_to(:action => 'index')
   else
   render('new')
   end
  end

  def edit
  @category = Category.find(params[:id])
  end
	def update
	@category = Category.find(params[:id])
  if @category.update_attributes(category_params)
    redirect_to(:action => 'show', :id => @category.id)
  else
    render('index')
  end	
	end
	def destroy
	Category.find(params[:id]).destroy
  redirect_to(:action => 'index')
	end
  def delete
  @category = Category.find(params[:id])
  end
  private
  def category_params
   params.require(:category).permit(:name, :thumburl)
   end
end

########New View
<%= render 'shared/topnav' %>
<%= render 'form' %>
<h1>New Category</h1>

<!-- Render form here -->

<%= link_to 'Back', categories_path %>

<%= render 'shared/footer' %>

########Edit and Update Methods
class CategoriesController < ApplicationController
  def index
   @categories = Category.all
  end

  def show
   @category = Category.find(params[:id])
  end

  def new
  @category = Category.new
  end
  def create 
  @category = Category.new(category_params)
  if @category.save
   redirect_to(:action => 'index')
   else
   render('new')
   end
  end

  def edit
  @category = Category.find(params[:id])
  end
	def update
	@category = Category.find(params[:id])
  if @category.update_attributes(category_params)
    redirect_to(:action => 'show', :id => @category.id)
  else
    render('index')
  end	
	end
	def destroy
	Category.find(params[:id]).destroy
  redirect_to(:action => 'index')
	end
  def delete
  @category = Category.find(params[:id])
  end
  private
  def category_params
   params.require(:category).permit(:name, :thumburl)
   end
end

########Edit View
<%= render 'shared/topnav' %>

<h1>Edit Category</h1>

<!-- Render form here -->
<%= render 'form' %>
<%= link_to 'Back', categories_path %>

<%= render 'shared/footer' %>

########Delete and Destroy Methods
class CategoriesController < ApplicationController
  def index
   @categories = Category.all
  end

  def show
   @category = Category.find(params[:id])
  end

  def new
  @category = Category.new
  end
  def create 
  @category = Category.new(category_params)
  if @category.save
   redirect_to(:action => 'index')
   else
   render('new')
   end
  end

  def edit
  @category = Category.find(params[:id])
  end
	def update
	@category = Category.find(params[:id])
  if @category.update_attributes(category_params)
    redirect_to(:action => 'show', :id => @category.id)
  else
    render('index')
  end	
	end
	def destroy
	Category.find(params[:id]).destroy
  redirect_to(:action => 'index')
	end
  def delete
  @category = Category.find(params[:id])
  end
  private
  def category_params
   params.require(:category).permit(:name, :thumburl)
   end
end

########Delete View
<p>
  <strong>Name:</strong>
  <%= @category.name %>
</p>

<p>
  <strong>Thumburl:</strong>
  <%= image_tag @category.thumburl %>
</p>

<%= link_to "Delete", categories_delete_path(:id => @category.id) %> |
<%= link_to 'Edit', edit_category_path(@category) %> |
<%= link_to 'Back', categories_path %>


