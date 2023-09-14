abcd
Problemet jag stöttte på i den här uppgiften var hur jag kan bygga abcd. Jag visste att jag ska loopa 
igenom talen med hjälp av for loop och range funktionen och ha for loopen indenterade för att kunna få 
alla möjliga kompinationer av abcd. Efter att ha försökt bygga talen i en och samma funktion, jag gav 
upp och använde mig av en till funktion som heter get_nummber som tar emot 4 args och byggar ett tal
med desssa args. Sista delen var enklast som är att jämföra talen med if sats.

birthday_candles
Den uppgiften var svårast i assigenment två. 

countdigits
skapa till if satster som tar hand om inputen, skapa tre variabler som sätts lika med 0 som incrementeras
med ett ifall if satsen krav uppfylls

drunken_sailor
Började med att skapa variabler för grid, step och antal sailor. Värdet av dem anges av user i form av input.
Har även skapat dry and wet sailor för att hålla koll på antal sailor som hämnar utanför vår grid. För att
hålla koll på current_place har jag använt en dict. dict har endast två keys : X och Y vilket motsvarar 
x-axel samt y-axel. Value för dem kan höjs eller sänks med ett steg beroande på sailor har tagit ett steg
framåt eller bakåt. I for loopet kontroleras sailor place ifall den har hämnat utanför grid och incrementeras
värdet av wet med 1 annars incrementeras dry med 1. 

salary_revision
Skapa två funktioner user_input och revision. Första funktionen tar hand om input user och omvandlar det till
en lista av salaries med hjälp av split() method. Där efter skapa en for loop som konverterar våra tal från 
str till int annars retuneras en fel medelande.  