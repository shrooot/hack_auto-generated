require 'rest-client'

class MainController < ApplicationController
  def index

  end

  def analyze
    @message = params[:message]
    puts @message
    response = get_sentiment(@message)

    render :result, locals: { message: @message, result: response}

    # redirect_to result_path message: message
  end

  private


  def get_sentiment(message)
    response = RestClient.post("http://localhost:8080/sentiment", {text: message}.to_json, headers = {"Content-Type": "application/json", "Accept": "application/json"})

    JSON.parse(response.body)
  end
end
