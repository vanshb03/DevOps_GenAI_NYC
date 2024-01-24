import { NavBar } from './components/navbar.components'

function App() {

  return (
    <>
      <NavBar />
      <div className="min-h-full flex">
        <div className="lg:pl-64 flex flex-col w-0 flex-1">

          <main className="flex-1">
            <div className="py-8 xl:py-10">
              <form 
                className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 xl:max-w-7xl xl:grid xl:grid-cols-3"
              >
                <div className='xl:col-span-2 xl:pr-8 xl:border-r xl:border-gray-200 max-h-screen'> 
                  <div>
                    <div>
                      <div className=" md:space-x-4 xl:pb-3">
                                              
                        <div class="mx-auto p-4">
                          <div class="bg-white rounded-lg shadow-md p-4">
                            <div class="flex items-center mb-4">
                              <div class="ml-3">
                                <p class="text-xl font-medium">Your AI Tutor</p>
                                <p class="text-gray-500">Online</p>
                              </div>
                            </div>

                            <div class="space-y-4 min-h-full pb-20">
                              <div class="flex items-start">
                              <img src="https://dummyimage.com/50x50.png?text=AI" alt="Other User Avatar" class="w-8 h-8 rounded-full ml-3" />
                                <div class="ml-3 bg-gray-100 p-3 rounded-lg">
                                  <p class="text-sm text-gray-800">Hello! How can I help you today?</p>
                                </div>
                              </div>

                              <div class="flex items-end justify-end">
                                <div class="bg-blue-500 p-3 rounded-lg">
                                  <p class="text-sm text-white">Sure, I have a question.</p>
                                </div>
                                <img src="https://dummyimage.com/50x50.png?text=U" alt="Other User Avatar" class="w-8 h-8 rounded-full ml-3" />
                              </div>
                            </div>

                            
                            <div class="mt-4 flex items-center">
                              <input
                                type="text"
                                placeholder="Type your message..."
                                class="flex-1 py-2 px-3 rounded-full bg-gray-100 focus:outline-none"
                              />
                              <button class="bg-blue-500 text-white px-4 py-2 rounded-full ml-3 hover:bg-blue-600">Send</button>
                            </div>
                          </div>
                        </div>
                      </div>

                        <aside className="mt-8 xl:hidden">
                        <div className="space-y-5">
                            <div className="flex items-center space-x-2">
                              <span className="text-gray-900 text-4xl font-medium">Model Understanding</span>
                            </div>
                            
                            <div className="flex items-center space-x-2">
                              <span className="text-gray-900 text-sm font-medium">
                              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
                              </span>
                            </div>
                        </div>
                      </aside>
                    </div>
                  </div>
                </div>
                
                  <aside className="hidden xl:block xl:pl-8">
                    <h2 className="sr-only">Score</h2>
                    <div className="space-y-5">
                      <div className="flex items-center space-x-2">
                        <span className="text-gray-900 text-4xl font-medium">Model Understanding</span>
                      </div>
                      <div className="flex items-center space-x-2">
                        <span className="text-gray-900 text-sm font-medium">
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
                        </span>
                      </div>
                    </div>
                  </aside>

              </form>
            </div>
          </main>
        </div>
      </div>
    </>
  );
}

export default App;
