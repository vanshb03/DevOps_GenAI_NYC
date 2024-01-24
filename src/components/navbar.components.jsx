export const NavBar = () => {
  return (
    <nav as="nav" className="bg-gray-800">
        <>
          <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <div className="flex h-16 justify-between">
              <div className="flex">
                <div className="flex flex-shrink-0 text-white items-center">
                  <p className="block text-lg h-8 w-auto lg:hidden">
                    Tutor-Ai
                  </p>
                  <p
                    className="hidden text-2xl h-8 w-auto lg:block">
                    Tutor-Ai
                    </p>
                </div>
              </div>
              <div className="flex items-center">
                <div className="flex-shrink-0">
                  <button
                    type="button"
                    className="relative inline-flex items-center rounded-md border border-transparent bg-indigo-500 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-indigo-600 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 focus:ring-offset-gray-800"
                  >
                    <span>Sign In</span>
                  </button>
                </div>
              </div>
            </div>
          </div>


        </>
    </nav>
  )
}
