# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    a.py                                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tkitagaw <tkitagaw@student.42.jp>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/05/30 15:44:32 by tkitagaw          #+#    #+#              #
#    Updated: 2020/05/30 15:50:39 by tkitagaw         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

s = [input() for i in range(2)]

if s[0] == s[1]:
    print("same")
elif s[0].lower() == s[1].lower():
    print("case-insensitive")
else:
    print("different")
