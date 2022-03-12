originalBatch = 48 
originalSugar = 1.5
originalButter = 1.0
originalFlour = 2.75

batchSize = float ( input("Enter the desired number of cookies: ") ) \

apsSugar = originalSugar / originalBatch 
apsButter = originalButter / originalBatch
apsFlour = originalFlour / originalBatch

newSugar = apsSugar * batchSize
newButter = apsButter * batchSize
newFlour = apsFlour * batchSize

print ( "Number of cups of flour:" + str(newFlour)) 
print ( "Number of cups of butter:" + str(newButter)) 
print ( "Number of cups of sugar:" + str(newSugar))


