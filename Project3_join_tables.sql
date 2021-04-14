use chinook;
select C.CustomerId, C.LastName, C.FirstName, T.Name, A.Title from Customer C
left join Invoice I on C.CustomerId = I.CustomerId
left join InvoiceLine IL on I.InvoiceId = IL.InvoiceId
left join Track T on T.TrackId = IL.TrackId
join Album A on T.AlbumId = A.AlbumId;
