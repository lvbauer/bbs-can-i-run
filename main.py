import streamlit as st
import itertools
import json

# position name as key and list of values indicating labels


PARTY_VAL = "party"
GOV_VAL = "government"

LEG_VAL = "legislature"
EXEC_VAL = "executive"
JUD_VAL = "judicial"

CITY_VAL = "city"
COUNTY_VAL = "county"
STATE_VAL = "state"

ELECTED_VAL = "elected"
APPOINTED_VAL = "appointed"


POSITION_DICT = {

    # Legislative
    "City Council Member (City|Government|Legislative|Elected)" : [GOV_VAL, LEG_VAL, CITY_VAL, ELECTED_VAL],
    
    "County Supervisor (County|Government|Legislative|Elected)" : [GOV_VAL, LEG_VAL, COUNTY_VAL, ELECTED_VAL],
    
    "State Senator (State|Government|Legislative|Elected)" : [GOV_VAL, LEG_VAL, STATE_VAL, ELECTED_VAL],
    "State Representative (State|Government|Legislative|Elected)" : [GOV_VAL, LEG_VAL, STATE_VAL, ELECTED_VAL],

    # Executive
    "Mayor (City|Government|Executive|Elected)" : [CITY_VAL, GOV_VAL, LEG_VAL, ELECTED_VAL],
    "City Clerk (City|Government|Executive|Elected)" : [CITY_VAL, GOV_VAL, LEG_VAL, ELECTED_VAL],
    "City Treasurer (City|Government|Executive|Elected)" : [CITY_VAL, GOV_VAL, LEG_VAL, ELECTED_VAL],

    "County Executive (County|Government|Executive|Elected)" : [COUNTY_VAL, GOV_VAL, LEG_VAL, ELECTED_VAL],
    "Sheriff (County|Government|Executive|Elected)" : [COUNTY_VAL, GOV_VAL, LEG_VAL, ELECTED_VAL],
    "County Clerk (County|Government|Executive|Elected)" : [COUNTY_VAL, GOV_VAL, LEG_VAL, ELECTED_VAL],
    "County Treasurer (County|Government|Executive|Elected)" : [COUNTY_VAL, GOV_VAL, LEG_VAL, ELECTED_VAL],
    "School Board Member (County|Government|Executive|Elected)" : [COUNTY_VAL, GOV_VAL, LEG_VAL, ELECTED_VAL],

    "Governor (State|Government|Executive|Elected)" : [STATE_VAL, GOV_VAL, LEG_VAL, ELECTED_VAL],
    "Lieutenant Governor (State|Government|Executive|Elected)" : [STATE_VAL, GOV_VAL, LEG_VAL, ELECTED_VAL],
    "Secretary of State (State|Government|Executive|Elected)" : [STATE_VAL, GOV_VAL, LEG_VAL, ELECTED_VAL],
    "State Treasurer (State|Government|Executive|Elected)" : [STATE_VAL, GOV_VAL, LEG_VAL, ELECTED_VAL],
    "Super. of Public Instruction (State|Government|Executive|Elected)" : [STATE_VAL, GOV_VAL, LEG_VAL, ELECTED_VAL],


    # Judicial

    "City Attorney (City|Government|Judicial|Elected)" : [CITY_VAL, GOV_VAL, JUD_VAL, ELECTED_VAL],
    "Municipal Court Judge (City|Government|Judicial|Elected)" : [CITY_VAL, GOV_VAL, JUD_VAL, ELECTED_VAL],

    "District Attorney (County|Government|Judicial|Elected)" : [COUNTY_VAL, GOV_VAL, JUD_VAL, ELECTED_VAL],
    "Circuit Court Judge (County|Government|Judicial|Elected)" : [COUNTY_VAL, GOV_VAL, JUD_VAL, ELECTED_VAL],

    "Attorney General (State|Government|Judicial|Elected)" : [STATE_VAL, GOV_VAL, JUD_VAL, ELECTED_VAL],
    "Justice of the Supreme Court (State|Government|Judicial|Elected)" : [STATE_VAL, GOV_VAL, JUD_VAL, ELECTED_VAL],

    # Party

    "City Party Chair (City|Party|Elected)" : [CITY_VAL, PARTY_VAL, None, ELECTED_VAL],
    "City Party Secretary (City|Party|Elected)" : [CITY_VAL, PARTY_VAL, None, ELECTED_VAL],
    "City Party Campaign Manager (City|Party|Elected)" : [CITY_VAL, PARTY_VAL, None, ELECTED_VAL],

    "County Party Chair (County|Party|Elected)" : [COUNTY_VAL, PARTY_VAL, None, ELECTED_VAL],
    "County Party Secretary (County|Party|Elected)" : [COUNTY_VAL, PARTY_VAL, None, ELECTED_VAL],
    "County Party Campaign Manager (County|Party|Elected)" : [COUNTY_VAL, PARTY_VAL, None, ELECTED_VAL],

    "State Party Chair (State|Party|Elected)" : [STATE_VAL, PARTY_VAL, None, ELECTED_VAL],
    "State Party Secretary (State|Party|Elected)" : [STATE_VAL, PARTY_VAL, None, ELECTED_VAL],
    "State Party Campaign Manager (State|Party|Elected)" : [STATE_VAL, PARTY_VAL, None, ELECTED_VAL],

}

CODE_STAT_1_14_s3 = "statute1.14s3"
CODE_STAT_1_14_s4 = "statute1.14s4"
CODE_STAT_1_14_s5 = "statute1.14s5"
CODE_WARN_HIGHER_OFFICE = "higher_office"

def statute_1_14_sect_3(position_combination):

    #print(position_combination)

    for i, pos1 in enumerate(position_combination):


        pos1_list = POSITION_DICT[pos1]

        #st.write(pos1)

        if (STATE_VAL in pos1_list) and (PARTY_VAL in pos1_list) and (ELECTED_VAL in pos1_list):

            for j, pos2 in enumerate(position_combination):

                #st.write(pos2)

                pos2_list = POSITION_DICT[pos2]

                if (pos1 == pos2):
                    continue

                if (STATE_VAL in pos2_list) and (GOV_VAL in pos2_list):

                    print("statute 1.14s3 error")

                    return CODE_STAT_1_14_s3
                
    return None

def statute_1_14_sect_4(position_combination):


    for i, pos1 in enumerate(position_combination):

        pos1_list = POSITION_DICT[pos1]

        if (STATE_VAL in pos1_list) and (LEG_VAL in pos1_list):

            for j, pos2 in enumerate(position_combination):

                #st.write(pos2)

                pos2_list = POSITION_DICT[pos2]

                if (pos1 == pos2):
                    continue

                if (GOV_VAL in pos2_list) and ((CITY_VAL in pos2_list) or (COUNTY_VAL in pos2_list)):

                    #print("statute 1.14s4 error")
                    return CODE_STAT_1_14_s4
    return None

def statute_1_14_sect_5(position_combination):


    for i, pos1 in enumerate(position_combination):

        pos1_list = POSITION_DICT[pos1]

        for j, pos2 in enumerate(position_combination):

            pos2_list = POSITION_DICT[pos2]

            if (pos1 == pos2):
                continue

            if (CITY_VAL in pos1_list) and (CITY_VAL in pos2_list):
                return CODE_STAT_1_14_s5
            
            if (COUNTY_VAL in pos1_list) and (COUNTY_VAL in pos2_list):
                return CODE_STAT_1_14_s5
            
            if ((CITY_VAL in pos1_list) and (COUNTY_VAL in pos2_list)) or ((COUNTY_VAL in pos1_list) and (CITY_VAL in pos2_list)):
                return CODE_WARN_HIGHER_OFFICE


    return None

def main():

    st.title("BBS: Can I run?")

    st.subheader("Step 1: Select Potential Postions")
    user_selected_positions = st.multiselect("Positions", POSITION_DICT.keys())

    combination_list = itertools.combinations(user_selected_positions, 2)
    combination_list = [x for x in combination_list]

    conflict_list = []



    for comb_idx, comb in enumerate(combination_list):
        s1_14_s3 = statute_1_14_sect_3(comb)
        s1_14_s4 = statute_1_14_sect_4(comb)
        s1_14_s5 = statute_1_14_sect_5(comb)

        out_list = [s1_14_s3, s1_14_s4, s1_14_s5]

        while None in out_list:
            out_list.remove(None)

        if len(out_list) == 0:
            out_list = None

        conflict_list.append(out_list)

    with st.expander("test"):
        st.code(combination_list)
        st.code(conflict_list)

    st.subheader("Step 2: View Conflicts")

    for comb_out in conflict_list:
        if comb_out != None:
            st.warning("There are conflicts in selected positions.")
            break

    zip_comb = zip(combination_list, conflict_list)
    for idx, zip_item in enumerate(zip_comb):
        
        comb, results = zip_item

        st.subheader("Conflicts Between: " + comb[0] + " and " + comb[1])

        if results == None:
            st.success("This combination of positions does not have any conflicts. If one position is higher, it may be necessary to relinquish your lower position.")
            continue

        if CODE_STAT_1_14_s3 in results:
            st.error("This combination violates Statute 1.14 Section 3.")

        if CODE_STAT_1_14_s4 in results:
            st.error("This combination violates Statute 1.14 Section 4.")

        if CODE_STAT_1_14_s5 in results:
            st.error("This combination violates Statute 1.14 Section 5.")

        if CODE_WARN_HIGHER_OFFICE in results:
            st.warning("While no formal conflict exists, it may be necessary to relinquish your city office in favor of your county office.")
    

    print(conflict_list)


    pass

if __name__ == "__main__":
    main()
