# for locations without a public ranking in the past x days, do the ranking

# PUBLIC RANKINGS

# p_i is pr(i>average_bar)
# set p_i empirical winning % and 0.5 if not voted
# pr(i>>j) = f(p_i-p_j)
# set p_0 = empirical winning % (e.g assume all other bars are average)
# for all cha chas in bars:
#  Cha Cha beat k p_k^n
#  Cha Cha beat l p_l^n
#  Cha Cha lost j p_j^n
#  choose p_cc^n+1= max likelihood assuming independence given obs (1,p_cc^n+1p_k^n),(1,p_cc^n+1-
#   p_l^n),(0,p_cc^n+1-p_j^n)
# update and iterate until p_i for a city are done
# rankings are just the sorted p_i

# PERSONALIZED RANKINGS
# Random forests
# vector of features
# - classification problem (1 won or not or 0) - average across photos? 1=liked more often than not, how to get intensity of likes? % of wins
# - person characteristics (integer coded location for example, age, potentially college indicators in location (UCLA,USC))
# - don't forget instagram (is vain person, media, follow, followers)
# - linear time characteristc? or just use recent, last month data
# - bar characteristics i and j (essentially embedding others votes as constants, including bar_ids as integers)
# final score projected from p_j=some bar

# BATTLES NOTES
# ensure person doesn't vote on same photo
# should sample uniformly (if bar has more than x pics) to ensure precision
# eg cycle through bars best photo before getting photos