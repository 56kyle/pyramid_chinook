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
        <tr>
            <td> ${employee_id} </td>
            <td> ${last_name} </td>
            <td> ${first_name} </td>
            <td> ${title} </td>
            <td> ${reports_to} </td>
            <td> ${birth_date} </td>
            <td> ${hire_date} </td>
            <td> ${address} </td>
            <td> ${city} </td>
            <td> ${state} </td>
            <td> ${country} </td>
            <td> ${postal_code} </td>
            <td> ${phone} </td>
            <td> ${fax} </td>
            <td> ${email} </td>
        </tr>
    </table>
</div>
