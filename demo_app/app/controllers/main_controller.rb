class MainController < ApplicationController
  def index

  end

  def analyze
    message = params[:message]
    puts message
    #response = get_sentiment(message)

    render :result, locals: {message: message}

    # redirect_to result_path message: message
  end

  private


  def get_sentiment(message)
    response = RestClient.post("url", {message: message})
    JSON.parse(response.body)
  end
end
