-- GridWise AU: Add our first electricity market region

INSERT INTO public.regions (region_code, region_name)
VALUES ('NSW1', 'New South Wales and ACT');

-- Check the regions stored in our database
SELECT * FROM public.regions;