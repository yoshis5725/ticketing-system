'use client'

import React, {ReactNode, useContext, useState} from "react";


interface SearchContextType {
    search: string;
    setSearch: (search: string) => void;
}


const SearchContext = React.createContext<SearchContextType | undefined>(undefined);


export const SearchProvider = ({children}: { children: ReactNode }) => {
    const [search, setSearch] = useState('')

    return (
        <SearchContext.Provider value={{search, setSearch}}>
            {children}
        </SearchContext.Provider>
    )
}

export const useSearch = () => {
    const context = useContext(SearchContext)

    if (!context)
        throw new Error('useSearch must be used within the context')

    return context
}