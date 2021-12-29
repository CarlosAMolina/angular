## What is it?

Project to learn Angular.

## Run

```bash
cd PROJECT-FOLDER
npm install # Install node packages if it is the first time
ng serve --port 4200 --open
```

## Build

```bash
ng build
```

The folder `dist` has been created. To use its files:

```bash
cd dist
ng serve --port 4200 --open
```

## Deploy

The `index.html` file must have this value:

```bash
    <base href="." />
```

Not this one:

```bash
    <base href="/" />
```


## References

- Set up

  <https://angular.io/guide/setup-local>

- Build

  <https://angular.io/start/start-deployment>

