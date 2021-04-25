<%inherit file="layout.mako"/>
<div class="content">
    <table>
        <tr>
            <th>ID</th>
            <th>Last Name</th>
            <th>First Name</th>
            <th>Title</th>
            <th>Reports To</th>
            <th>Birth Date</th>
            <th>Hire Date</th>
            <th>Address</th>
            <th>City</th>
            <th>State</th>
            <th>Country</th>
            <th>Postal Code</th>
            <th>Phone</th>
            <th>Fax</th>
            <th>Email</th>
        </tr>
        % for employee in employees:
            <tr>
                <td>${employee.EmployeeId}</td>
                <td>${employee.LastName}</td>
                <td>${employee.FirstName}</td>
                <td>${employee.Title}</td>
                <td>${employee.ReportsTo}</td>
                <td>${employee.BirthDate}</td>
                <td>${employee.HireDate}</td>
                <td>${employee.Address}</td>
                <td>${employee.City}</td>
                <td>${employee.State}</td>
                <td>${employee.Country}</td>
                <td>${employee.PostalCode}</td>
                <td>${employee.Phone}</td>
                <td>${employee.Fax}</td>
                <td>${employee.Email}</td>
            </tr>
        % endfor
    </table>
</div>
