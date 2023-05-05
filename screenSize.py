def ScreenSize(screenWidth, screenHeight, appSizeW, appSizeH):
    # Calculate the width and height of the app based on the screen size and app size ratio
    appSizeW = screenWidth * appSizeW
    appSizeH = screenHeight * appSizeH

    # Calculate the remaining width and height of the screen after subtracting the app size
    remainingWidth = screenWidth - appSizeW
    remainingHight = screenHeight - appSizeH

    # Calculate the x and y position of the app to center it on the screen
    appWpos = remainingWidth / 2
    appHpos = remainingHight / 2

    # Create a tuple containing the app geometry in the form of "width x height + x position + y position"
    appGeometry = (
        int(appSizeW),
        "x",
        int(appSizeH),
        "+",
        int(appWpos),
        "+",
        int(appHpos),
    )

    # Remove any spaces, quotes, commas, parentheses from the app geometry string
    appGeometry = str(appGeometry).replace(" ", "")
    appGeometry = str(appGeometry).replace("'", "")
    appGeometry = str(appGeometry).replace(",", "")
    appGeometry = str(appGeometry).replace("(", "")
    appGeometry = str(appGeometry).replace(")", "")

    # Return the app geometry string
    return appGeometry
