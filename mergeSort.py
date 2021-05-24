class Solution:
# Best: O(nlog(n)) time | O(nlog(n)) space
# Average: O(nlog(n)) time | O(nlog(n)) space
# Worst: O(nlog(n)) time | O(nlog(n)) space

    def mergeSort(self, arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr)//2
        leftArr = arr[: mid]
        rightArr = arr[mid:]

        return self.mergeArrays(self.mergeSort(leftArr), self.mergeSort(rightArr))

    def mergeArrays(self, arr1, arr2):
        leftPtr, rightPtr = 0, 0
        result = []
        while leftPtr < len(arr1) and rightPtr < len(arr2):
            if arr1[leftPtr] < arr2[rightPtr]:
                result.append(arr1[leftPtr])
                leftPtr += 1
            else:
                result.append(arr2[rightPtr])
                rightPtr += 1

        if leftPtr < len(arr1):
            result += arr1[leftPtr:]

        if rightPtr < len(arr2):
            result += arr2[rightPtr:]
        return result


if __name__ == "__main__":
    unsortedArray = [8, 5, 2, 9, 5, 6, 3]  # [2, 3, 5, 5, 6, 8]
    # [1]
    # [1, 2]
    # [1, 2, 3]
    # [-10, -7, -7, -6, -6, -5, -5, -4, -4, -4, -2, -1, 1, 3, 5, 5, 6, 8, 8, 10]
    # [-10, -10, -9, -7, -7, -6, -5, -2, 2, 2, 3, 3, 4, 5, 8, 8, 9, 10]
    # [-10, -10, -9, -6, -5, -2, -2, -1, 1, 2, 4, 4, 6, 7, 7, 8, 8, 8, 8, 9, 10, 10]
    # [-10, -8, -6, -2, -2, -1, 1, 1, 2, 2, 3, 5, 9]
    # [-10, -10, -9, -9, -9, -8, -8, -6, -4, -4, -4, -2, -1,
    #  0, 0, 0, 0, 1, 1, 2, 2, 4, 4, 5, 5, 7, 8, 8, 9, 10]
    # [-9, -9, -9, -7, -7, -7, -4, -4, -3, -3, -3, -2, -1, 0, 1, 1, 3, 4, 4, 5, 8, 9]
    # [-991, -848, -764, -755, -710, -706, -646, -614, -610, -583, -484, -474, -439, -359, -348, -246, -215, -212, -171, -160, -153, -56, -
    #  32, -27, -3, 9, 12, 55, 107, 131, 222, 230, 240, 246, 427, 507, 564, 565, 568, 603, 635, 661, 710, 736, 787, 821, 892, 934, 970, 996]
    # [-998, -882, -827, -817, -796, -731, -681, -657, -581, -523, -435, -387, -382, -331, -269, -255, -220, -216, -169, -163, -75, -43, -6, 80,
    #  100, 180, 228, 280, 354, 366, 372, 382, 382, 432, 471, 519, 652, 680, 747, 749, 753, 769, 771, 805, 847, 906, 913, 956, 972, 980, 991]
    # [-995, -987, -978, -898, -796, -785, -772, -763, -755, -746, -720, -679, -626, -609, -581, -562, -559, -557, -544, -491, -489, -425, -389, -367, -343, -313, -112, -94, -86, -79, -68, -67, -19, -7,
    #  31, 34, 43, 51, 67, 85, 120, 165, 187, 204, 232, 243, 260, 384, 393, 397, 421, 432, 444, 489, 508, 515, 612, 624, 662, 687, 697, 732, 737, 759, 776, 777, 825, 878, 921, 924, 946, 947, 975, 993]
    # [-975, -947, -924, -917, -877, -810, -753, -739, -738, -731, -702, -685, -656, -655, -581, -578, -531, -500, -488, -401, -396, -359, -356, -320, -312, -279, -249, -154, -90, -54, -
    #  45, 61, 94, 150, 153, 153, 194, 195, 266, 329, 343, 376, 394, 399, 445, 452, 459, 464, 528, 544, 551, 556, 568, 669, 689, 713, 738, 748, 763, 788, 844, 867, 886, 904, 972, 993]
    # [-991, -976, -937, -917, -904, -885, -837, -821, -740, -641, -628, -609, -602, -599, -568, -560, -557, -529, -519, -453, -415, -384, -373, -321, -319, -220, -158, -96, -92, -90, -85, -67, -50, -36, -19, 63, 80, 121, 154, 168, 207,
    #  228, 254, 268, 268, 270, 294, 295, 296, 306, 307, 328, 351, 381, 387, 391, 401, 407, 434, 437, 491, 505, 518, 558, 588, 593, 607, 613, 619, 629, 676, 678, 718, 730, 753, 759, 798, 802, 834, 879, 881, 896, 915, 937, 946, 949, 986]
    # [-987, -950, -949, -942, -941, -935, -908, -874, -855, -846, -823, -817, -796, -738, -733, -730, -685, -578, -575, -575, -544, -542, -469, -441, -420, -415, -410, -376, -371, -363, -359, -353, -337, -293, -265, -257, -254, -191, -167, -
    #  160, -155, -126, -120, -51, -36, -13, 14, 48, 52, 59, 59, 125, 157, 164, 183, 201, 238, 243, 295, 323, 328, 341, 355, 356, 372, 399, 422, 490, 490, 540, 572, 610, 631, 646, 700, 724, 746, 800, 829, 842, 888, 892, 892, 919, 950, 965, 980, 995]

print(Solution().mergeSort(unsortedArray))


# solution 2
# Best: O(nlog(n)) time | O(n) space
# Average: O(nlog(n)) time | O(n) space
# Worst: O(nlog(n)) time | O(n) space

def mergeSort(array):
    if len(array) <= 1:
        return array
    auxiliaryArray = array[:]
    mergeSortHelper(array, 0, len(array)-1, auxiliaryArray)
    return array


def mergeSortHelper(mainArray, startIdx, endIdx, auxiliaryArray):
    if startIdx == endIdx:
        return
    middleIdx = (startIdx+endIdx) // 2
    mergeSortHelper(auxiliaryArray, startIdx, middleIdx, mainArray)
    mergeSortHelper(auxiliaryArray, middleIdx+1, endIdx, mainArray)
    doMerge(mainArray, startIdx, middleIdx, endIdx, auxiliaryArray)


def doMerge(mainArray, startIdx, middleIdx, endIdx, auxiliaryArray):
    k = startIdx
    i = startIdx
    j = middleIdx + 1
    while i <= middleIdx and j <= endIdx:
        if auxiliaryArray[i] <= auxiliaryArray[j]:
            mainArray[k] = auxiliaryArray[i]
            i += 1
        else:
            mainArray[k] = auxiliaryArray[j]
            j += 1
        k += 1
    while i <= middleIdx:
        mainArray[k] = auxiliaryArray[i]
        i += 1
        k += 1
    while j <= endIdx:
        mainArray[k] = auxiliaryArray[j]
        j += 1
        k += 1
