# Create a function
def insert_case(row, driver):
    # Insert Case ID
    # wait until page loads
    WebDriverWait(driver, 10).until(lambda driver: driver.find_element(By.ID, "PatientId").is_displayed())
    case_id = driver.find_element(By.ID, "PatientId")
    case_id.clear()
    case_id.send_keys(str(row['MRN']))
    # Insert Date
    date = driver.find_element(By.ID, "ProcedureDate")
    date.click()
    date.clear()
    date.send_keys(str(row['Date']))
    # Attending
    attending = driver.find_element(By.ID, "select2-Attendings-container")
    attending.click()
    attending_name = driver.find_element(By.XPATH, '/html/body/span[2]/span/span[1]/input')
    surgeon_firstword = row['Surgeons'].split(' ')[0]
    surgeon_firstword = surgeon_firstword.replace(',', '')
    attending_name.clear()
    attending_name.send_keys(surgeon_firstword)
    attending_name.send_keys(u'\ue007')
    # Procedure
    # Use regex to extract the CPT codes from the procedure field which are in brackets
    import re
    CPTs = re.findall(r'\[(.*?)\]', row['Panel Procedure Codes'])
    # Loop backwards so that the first code is last and gets selected as primary
    for CPT in reversed(CPTs):
        driver.find_element(By.XPATH,'//*[@id="tabs"]/li[2]/a').click()
        code_description = driver.find_element(By.ID, "CodeDescription")
        code_description.clear()
        code_description.send_keys(CPT)
        code_description.send_keys(u'\ue007')
        driver.find_element(By.XPATH,'//*[@id="code-qty"]/button').click()
        driver.find_element(By.XPATH,'//*[@id="IsCredit"]').click()
    time.sleep(1)
    driver.find_element(By.ID,'submitButton').click()
    # Check if there is an error
    message = ''
    try:
        error = driver.find_element(By.ID,'server-errors')
        message = error.text
    except:
        message = 'Added successfully.'
    print(message)
