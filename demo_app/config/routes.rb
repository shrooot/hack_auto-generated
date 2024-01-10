Rails.application.routes.draw do
  # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html

  # Reveal health status on /up that returns 200 if the app boots with no exceptions, otherwise 500.
  # Can be used by load balancers and uptime monitors to verify that the app is live.
  get 'up' => 'rails/health#show', as: :rails_health_check

  # Defines the root path route ("/")
  # root "posts#index"

  # "to" points to the controller and the first one is the name and the second one is the function
  # inside the controller, read as "main" controller and "index" action
  # it will look for a file named main_controller inside controller folder

  root to: 'main#index'
  post '/', to: 'main#analyze'

  # get '/result', to: 'result#index'
end
